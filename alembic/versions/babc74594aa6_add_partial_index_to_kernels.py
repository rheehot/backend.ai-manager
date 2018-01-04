"""add-partial-index-to-kernels

Revision ID: babc74594aa6
Revises: c3e74dcf1808
Create Date: 2018-01-04 14:33:39.173062

"""
from alembic import op
import sqlalchemy as sa
import ai.backend.manager.models.base


# revision identifiers, used by Alembic.
revision = 'babc74594aa6'
down_revision = 'c3e74dcf1808'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index(
        op.f('ix_kernels_unique_sess_token'),
        'kernels', ['access_key', 'sess_id'],
        unique=True,
        postgresql_where=sa.text("kernels.status != 'TERMINATED'"),
    )


def downgrade():
    op.drop_index(op.f('ix_kernels_unique_sess_token'), table_name='kernels')
