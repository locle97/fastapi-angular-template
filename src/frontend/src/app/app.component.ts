import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { environment } from '../environments/environment';
import { FormsModule } from '@angular/forms';

class Item {
  id: number = 0;
  name: string = '';
  completed: boolean = false;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, HttpClientModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  apiUrl = environment.apiUrl;
  newItemName: string = '';
  items: Item[] = [];

  constructor(private _httpClient: HttpClient) {
    this.loadItems();
  }

  ngOnInit(): void { }

  loadItems() {
    const url = this.apiUrl + '/items';

    this._httpClient.get<Item[]>(url).subscribe((res) => {
      this.items = res;
    });
  }

  addItem() {
    console.log(`Adding item: ${this.newItemName}`);
  }

  completeItem(item: Item) {
    item.completed = !item.completed;
  }

  removeItem(item: Item) {
    console.log(`Removing item: ${item.id}`);
  }
}
