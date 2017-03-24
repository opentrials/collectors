# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b32475938a2d'
down_revision = u'542425c4e70b'
branch_labels = None
depends_on = None

updatable_tables = ['actrn', 'cochrane_reviews', 'euctr', 'fda_dap', 'fdadl', 'gsk',
    'hra', 'icdcm', 'icdpcs', 'ictrp', 'isrctn', 'jprn', 'nct', 'pfizer', 'pubmed', 'takeda']


def upgrade():
    conn = op.get_bind()
    func = sa.DDL("""CREATE FUNCTION set_meta_updated()
                      RETURNS TRIGGER
                      LANGUAGE plpgsql
                    AS $$
                    BEGIN
                      NEW.meta_updated := now();
                      RETURN NEW;
                    END;
                    $$;""")
    conn.execute(func)

    for table in updatable_tables:
        trigger_params = {'trigger': ('%s_set_meta_updated' % table), 'table': table}
        trigger = ("""CREATE TRIGGER %(trigger)s
                    BEFORE UPDATE ON %(table)s
                    FOR EACH ROW EXECUTE PROCEDURE set_meta_updated();""" % trigger_params)
        conn.execute(trigger)


def downgrade():
    conn = op.get_bind()
    for table in updatable_tables:
        trigger_params = {'trigger': ('%s_set_meta_updated' % table), 'table': table}
        trigger = ('DROP TRIGGER %(trigger)s ON %(table)s;' % trigger_params)
        conn.execute(trigger)

    conn.execute(sa.DDL('DROP FUNCTION set_meta_updated();'))
