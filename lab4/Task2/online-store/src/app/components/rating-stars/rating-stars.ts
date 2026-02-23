import {Component, Input} from '@angular/core';
import {PRODUCTS} from '../../data/products.data';
import {Product} from '../../models/product.model'

@Component({
  selector: 'app-rating-stars',
  imports: [],
  templateUrl: './rating-stars.html',
  styleUrl: './rating-stars.scss',
})
export class RatingStars {
  @Input() product!: Product;

  products = PRODUCTS;

  getStarsArray(): number[] {
    const count = Math.floor(this.product.rating);
    return Array(count).fill(0).map((_, i) => i);
  }
}
