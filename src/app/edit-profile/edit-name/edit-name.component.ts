import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-name',
  templateUrl: './edit-name.component.html',
  styleUrls: ['./edit-name.component.scss']
})
export class EditNameComponent implements OnInit {
  userName:string = "Hanika";
  rename:boolean = false;
  constructor() { }

  ngOnInit(): void {
  }

  showRename(){
    this.rename = true;
  }

}
