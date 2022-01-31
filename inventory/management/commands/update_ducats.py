from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError
from inventory.models import Item
from inventory.utils import get_ducats_from_market


class Command(BaseCommand):
    help = 'Update Prime Items Ducat value'
    
    def add_arguments(self, parser) -> None:
        parser.add_argument('-f', '--force', default=False, action='store_true', help='Force update all IDs')
    
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        force = options['force']
        
        try:
            if force:
                items = Item.objects.filter(type='P')
            else:
                items = Item.objects.filter(type='P').filter(ducats=0)
            
            if items.exists():
                for item in items:
                    print(f'Updating ducats for: {item.name}')
                    item.ducats = get_ducats_from_market(item.url_name)
                    item.save()
            else:
                print(f'No updates needed')
                    
        except Exception as e:
            raise CommandError(e)
            
            