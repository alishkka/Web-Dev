import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; 
import { ProductListComponent } from './product-list/product-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ProductListComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  categories: string[] = ['All', 'Gaming & Laptops', 'Audio & Speakers', 'Photography & Accessories', 'Smartphones & Tablets'];
  selectedCategory: string = 'All';

  selectCategory(category: string) {
    this.selectedCategory = category;
  }
}
