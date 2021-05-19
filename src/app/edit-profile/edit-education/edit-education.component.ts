import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-education',
  templateUrl: './edit-education.component.html',
  styleUrls: ['./edit-education.component.scss']
})
export class EditEducationComponent implements OnInit {
  eduQuals = [["School1", "Secondary"], ["School2","Primary"]]
  addLinkClicked:boolean = false;
  constructor() { }

  ngOnInit(): void {
  }

  removeSchool(){
    //
  }
  showAddSchool(){
    this.addLinkClicked = true;
  }

}
