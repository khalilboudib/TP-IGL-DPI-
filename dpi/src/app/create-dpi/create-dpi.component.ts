import { Component } from '@angular/core';

@Component({
  selector: 'app-create-dpi',
  templateUrl: './create-dpi.component.html',
  styleUrls: ['./create-dpi.component.css']
})
export class CreateDpiComponent {
  createDpi(): void {
    console.log('New DPI Created');
  }
}
