import {Component, Input} from '@angular/core';
import {Product} from "../../models/product.model";
import {RatingStars} from '../rating-stars/rating-stars';

@Component({
  selector: 'app-product-card',
  imports: [
    RatingStars
  ],
  templateUrl: './product-card.html',
  styleUrl: './product-card.scss',
})
export class ProductCard {
  @Input() product!: Product;

  shareToTelegram() {
    const url = encodeURIComponent(this.product.link);
    const text = encodeURIComponent(`Check this out ${this.product.name}`);
    const telegramUrl = `https://t.me/share/url?url=${url}&text=${text}`

    window.open(telegramUrl, '_blank');
  }
}
