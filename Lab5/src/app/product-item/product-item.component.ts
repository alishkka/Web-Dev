import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common'; 

interface Product {
  name: string;
  description: string;
  rating: number;
  imageUrls: string[];
  link: string;
  likes: number;
  category: string;
}

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
  @Input() product!: Product;
  @Output() like = new EventEmitter<void>();
  @Output() remove = new EventEmitter<void>();

  likeProduct() {
    this.like.emit();
  }

  removeProduct() {
    this.remove.emit();
  }
}
