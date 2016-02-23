from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
kmp_entry = Table('kmp_entry', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=80)),
    Column('email', String(length=80)),
    Column('phone', String(length=20)),
    Column('guild', String(length=10)),
    Column('sitsit', Boolean),
    Column('station', String(length=10)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['kmp_entry'].columns['station'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['kmp_entry'].columns['station'].drop()