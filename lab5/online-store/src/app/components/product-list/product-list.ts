import {Component, Input} from '@angular/core';
import {ProductCard} from '../product-card/product-card';
import {CommonModule} from '@angular/common';
import {Product} from '../../models/product.model'

@Component({
  selector: 'app-product-list',
  imports: [
    ProductCard
  ],
  templateUrl: './product-list.html',
  styleUrl: './product-list.scss',
})
export class ProductList {
  @Input() products: Product[] = [];

  onProductDelete(productId: number): void {
    this.products = this.products.filter(product => product.id !== productId);
  }
}
