import sqlalchemy as sa
from .base import metadata, IDColumn

__all__ = ('agents', )


agents = sa.Table(
    'agents', metadata,
    sa.Column('id', sa.String(length=64), primary_key=True),

    sa.Column('mem_slots', sa.Integer(), nullable=False),        # in the unit of 256 MBytes
    sa.Column('cpu_slots', sa.Integer(), nullable=False),        # number of cores
    sa.Column('gpu_slots', sa.Integer(), nullable=False),        # 2 * number of GPU devices

    sa.Column('used_mem_slots', sa.Integer(), nullable=False),
    sa.Column('used_cpu_slots', sa.Integer(), nullable=False),
    sa.Column('used_gpu_slots', sa.Integer(), nullable=False),

    sa.Column('addr', sa.String(length=128), nullable=False),
    sa.Column('first_contact', sa.DateTime(timezone=True), server_default=sa.func.now()),
)