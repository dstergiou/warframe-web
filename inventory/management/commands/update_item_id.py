from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError
from inventory.models import Item
from inventory.utils import get_item_id_from_market


class Command(BaseCommand):
    help = 'Update item IDs as recorded on warframe.market'
    
    def add_arguments(self, parser) -> None:
        parser.add_argument('-f', '--force', default=False, action='store_true', help='Force update all IDs')
    
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        force = options['force']
        
        try:
            if force:
                items = Item.objects.all()
            else:
                items = Item.objects.filter(item_id = '__REPLACE__')
            
            if items.exists():
                for item in items:
                    print(f'Updating ID for: {item.name}')
                    item.item_id = get_item_id_from_market(item.url_name)
                    item.save()
            else:
                print(f'No updates needed')
                    
        except Exception as e:
            raise CommandError(e)
            
            