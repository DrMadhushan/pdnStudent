import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-experience',
  templateUrl: './edit-experience.component.html',
  styleUrls: ['./edit-experience.component.scss']
})
export class EditExperienceComponent implements OnInit {
  experiences = [["experience-1","sdfghjk"],["experience-2","sdfghjk sfajsdn dasdjasnd"]]
  addLinkClicked:boolean = false;
  
  
  constructor() { }

  ngOnInit(): void {
  }

  showAddExp(){
    this.addLinkClicked =true;
  }

  removeExperience(){
    //
  }

}
