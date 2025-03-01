import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; 

interface Product {
  name: string;
  description: string;
  rating: number;
  imageUrls: string[];
  link: string;
  likes: number;
}

interface Category {
  name: string;
  products: Product[];
}

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent {
  categories: Category[] = [
    {
      name: 'Gaming & Laptops',
      products: [
        {
          name: 'PlayStation 5',
          description: 'Next-gen gaming console by Sony.',
          rating: 4.9,
          imageUrls: ['https://example.com/ps5.jpg'],
          link: 'https://kaspi.kz/shop/p/sony-playstation-5',
          likes: 0
        },
        {
          name: 'Asus ROG Laptop',
          description: 'High-performance gaming laptop.',
          rating: 4.7,
          imageUrls: ['https://example.com/asus-rog.jpg'],
          link: 'https://kaspi.kz/shop/p/asus-rog-laptop',
          likes: 0
        },
        {
          name: 'Xbox Series X',
          description: 'Powerful gaming console by Microsoft.',
          rating: 4.8,
          imageUrls: ['https://example.com/xbox-series-x.jpg'],
          link: 'https://kaspi.kz/shop/p/xbox-series-x',
          likes: 0
        },
        {
          name: 'Lenovo Legion 5',
          description: 'Gaming laptop with RTX 4060.',
          rating: 4.6,
          imageUrls: ['https://example.com/lenovo-legion5.jpg'],
          link: 'https://kaspi.kz/shop/p/lenovo-legion-5',
          likes: 0
        },
        {
          name: 'Razer Blade 15',
          description: 'Premium gaming laptop with OLED display.',
          rating: 4.7,
          imageUrls: ['https://example.com/razer-blade15.jpg'],
          link: 'https://kaspi.kz/shop/p/razer-blade-15',
          likes: 0
        }
      ]
    },
    {
      name: 'Audio & Speakers',
      products: [
        {
          name: 'Sony WH-1000XM5',
          description: 'Premium noise-canceling headphones.',
          rating: 4.8,
          imageUrls: ['https://example.com/sony-headphones.jpg'],
          link: 'https://kaspi.kz/shop/p/sony-wh-1000xm5',
          likes: 0
        },
        {
          name: 'JBL Charge 5',
          description: 'Portable Bluetooth speaker.',
          rating: 4.6,
          imageUrls: ['https://example.com/jbl-charge5.jpg'],
          link: 'https://kaspi.kz/shop/p/jbl-charge-5',
          likes: 0
        },
        {
          name: 'Apple AirPods Pro 2',
          description: 'Wireless noise-canceling earbuds.',
          rating: 4.8,
          imageUrls: ['https://example.com/airpods-pro2.jpg'],
          link: 'https://kaspi.kz/shop/p/apple-airpods-pro-2',
          likes: 0
        },
        {
          name: 'Bose SoundLink Revolve+',
          description: '360-degree portable speaker.',
          rating: 4.7,
          imageUrls: ['https://example.com/bose-soundlink.jpg'],
          link: 'https://kaspi.kz/shop/p/bose-soundlink-revolve',
          likes: 0
        },
        {
          name: 'Marshall Emberton',
          description: 'Stylish Bluetooth speaker with bass boost.',
          rating: 4.6,
          imageUrls: ['https://example.com/marshall-emberton.jpg'],
          link: 'https://kaspi.kz/shop/p/marshall-emberton',
          likes: 0
        }
      ]
    },
    {
      name: 'Photography & Accessories',
      products: [
        {
          name: 'GoPro Hero 12',
          description: 'Action camera with 5K recording.',
          rating: 4.6,
          imageUrls: ['https://example.com/gopro-hero12.jpg'],
          link: 'https://kaspi.kz/shop/p/gopro-hero-12',
          likes: 0
        },
        {
          name: 'Canon EOS R6',
          description: 'Professional mirrorless camera.',
          rating: 4.8,
          imageUrls: ['https://example.com/canon-eosr6.jpg'],
          link: 'https://kaspi.kz/shop/p/canon-eos-r6',
          likes: 0
        },
        {
          name: 'DJI Mini 3 Pro',
          description: 'Compact drone with 4K camera.',
          rating: 4.7,
          imageUrls: ['https://example.com/dji-mini3.jpg'],
          link: 'https://kaspi.kz/shop/p/dji-mini-3-pro',
          likes: 0
        },
        {
          name: 'Sony Alpha A7 IV',
          description: 'Full-frame mirrorless camera.',
          rating: 4.9,
          imageUrls: ['https://example.com/sony-alpha7iv.jpg'],
          link: 'https://kaspi.kz/shop/p/sony-alpha-a7iv',
          likes: 0
        },
        {
          name: 'Zhiyun Weebill 3',
          description: 'Handheld gimbal for stabilizing video.',
          rating: 4.5,
          imageUrls: ['https://example.com/zhiyun-weebill3.jpg'],
          link: 'https://kaspi.kz/shop/p/zhiyun-weebill-3',
          likes: 0
        }
      ]
    },
    {
      name: 'Smartphones & Tablets',
      products: [
        {
          name: 'iPhone 15 Pro',
          description: 'Apple’s latest flagship smartphone.',
          rating: 4.9,
          imageUrls: ['https://example.com/iphone-15pro.jpg'],
          link: 'https://kaspi.kz/shop/p/iphone-15-pro',
          likes: 0
        },
        {
          name: 'Samsung Galaxy S23 Ultra',
          description: 'High-end Android smartphone.',
          rating: 4.8,
          imageUrls: ['https://example.com/samsung-s23-ultra.jpg'],
          link: 'https://kaspi.kz/shop/p/samsung-galaxy-s23-ultra',
          likes: 0
        },
        {
          name: 'Google Pixel 8 Pro',
          description: 'Google’s best AI-powered smartphone.',
          rating: 4.7,
          imageUrls: ['https://example.com/pixel-8-pro.jpg'],
          link: 'https://kaspi.kz/shop/p/google-pixel-8-pro',
          likes: 0
        },
        {
          name: 'iPad Pro M2',
          description: 'Apple tablet with M2 chip and 120Hz screen.',
          rating: 4.9,
          imageUrls: ['https://example.com/ipad-pro-m2.jpg'],
          link: 'https://kaspi.kz/shop/p/ipad-pro-m2',
          likes: 0
        },
        {
          name: 'Samsung Galaxy Tab S9',
          description: 'Premium Android tablet for productivity.',
          rating: 4.7,
          imageUrls: ['https://example.com/tab-s9.jpg'],
          link: 'https://kaspi.kz/shop/p/samsung-galaxy-tab-s9',
          likes: 0
        }
      ]
    }
  ];

  selectedCategory: Category | null = null;

  selectCategory(category: Category) {
    this.selectedCategory = category;
  }

  removeProduct(product: Product) {
    if (this.selectedCategory) {
      this.selectedCategory.products = this.selectedCategory.products.filter(p => p !== product);
    }
  }

  likeProduct(product: Product) {
    product.likes++;
  }
}
