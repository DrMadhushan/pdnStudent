import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-image',
  templateUrl: './edit-image.component.html',
  styleUrls: ['./edit-image.component.scss']
})
export class EditImageComponent implements OnInit {
  profileImg:string = "assets/img/profile-pic1.jpg";
  showUploadImg:boolean = false;
  constructor() { }

  ngOnInit(): void {
  }

  openUploadImg(){
    this.showUploadImg = true;
  }
}
