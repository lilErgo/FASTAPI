"""new date

Revision ID: fbbef7d34c12
Revises: 7e8464e38469
Create Date: 2026-02-05 15:13:45.833570

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fbbef7d34c12'
down_revision: Union[str, Sequence[str], None] = '7e8464e38469'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
