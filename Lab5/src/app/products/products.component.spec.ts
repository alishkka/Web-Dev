import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ProductsComponent } from './products.component';

describe('ProductsComponent', () => {
  let component: ProductsComponent;
  let fixture: ComponentFixture<ProductsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProductsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have categories', () => {
    expect(component.categories.length).toBe(4);
  });

  it('should select a category', () => {
    const testCategory = component.categories[0];
    component.selectCategory(testCategory);
    expect(component.selectedCategory).toBe(testCategory);
  });

  it('should increase likes', () => {
    const testProduct = component.categories[0].products[0];
    const initialLikes = testProduct.likes;
    component.likeProduct(testProduct);
    expect(testProduct.likes).toBe(initialLikes + 1);
  });

  it('should remove a product', () => {
    component.selectCategory(component.categories[0]);
    const initialLength = component.selectedCategory!.products.length;
    component.removeProduct(component.selectedCategory!.products[0]);
    expect(component.selectedCategory!.products.length).toBe(initialLength - 1);
  });
});
