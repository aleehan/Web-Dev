import {Component, Input, Output, EventEmitter} from '@angular/core';
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
  @Output() delete = new EventEmitter<number>();

  onLike() {
    this.product.likes++;
  }

  onDelete() {
    if(confirm(`Are you sure you want to delete ${this.product.name}?`)) {
      this.delete.emit(this.product.id);
    }
  }

  shareToTelegram() {
    const url = encodeURIComponent(this.product.link);
    const text = encodeURIComponent(`Check this out ${this.product.name}`);
    const telegramUrl = `https://t.me/share/url?url=${url}&text=${text}`

    window.open(telegramUrl, '_blank');
  }
}
