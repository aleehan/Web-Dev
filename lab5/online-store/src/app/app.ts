import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {ProductCard} from './components/product-card/product-card';
import {ProductList} from './components/product-list/product-list';
import {Header} from './components/header/header';
import {PRODUCTS} from './data/products.data';
import {CATEGORIS} from './data/category.data';
import {Product} from './models/product.model';
import {Category} from './models/category.model';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ProductCard, ProductList, Header],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('online-store');
  allProducts: Product[] = PRODUCTS;
  categories: Category[] = CATEGORIS;

  selectedCategoryId: number | null = null;
  selectedProducts: Product[] = [];

  selectCategory(categoryId: number): void {
    this.selectedCategoryId = categoryId;
    this.selectedProducts = this.allProducts.filter(
      product => product.categoryId === categoryId
    );
  }

  isSelected(categoryId: number): boolean {
    return this.selectedCategoryId === categoryId;
  }
}
