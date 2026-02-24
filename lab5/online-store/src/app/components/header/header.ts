import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  imports: [],
  templateUrl: './header.html',
  styleUrl: './header.scss',
})
export class Header {
  menuItems = ['Home', 'Shop', 'Likes', 'About'];

  lineWidth = 0;
  lineLeft = 0;

  moveLine(element: HTMLElement) {
    // OffsetLeft is the position relative to the parent container
    this.lineLeft = element.offsetLeft;
    // OffsetWidth is the actual width of the text/li
    this.lineWidth = element.offsetWidth;
  }
}
