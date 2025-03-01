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

  it('should have a list of products', () => {
    expect(component.products.length).toBeGreaterThan(0);
  });

  it('should copy link to clipboard', () => {
    spyOn(navigator.clipboard, 'writeText');
    const testLink = 'https://example.com/test-product';
    component.copyLink(testLink);
    expect(navigator.clipboard.writeText).toHaveBeenCalledWith(testLink);
  });
});
