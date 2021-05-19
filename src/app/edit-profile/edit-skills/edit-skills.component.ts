import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-skills',
  templateUrl: './edit-skills.component.html',
  styleUrls: ['./edit-skills.component.scss']
})
export class EditSkillsComponent implements OnInit {
  skills = ["python","Java","python","Java","python","Java","python","Java","python","Java","python","Java","python","Java","python","Java","python","Java","Java","python","Java","python","Java"];
  addLinkClicked:boolean = false;
  constructor() { }

  ngOnInit(): void {
  }

  removeSkill(){
    this.skills[0] = "Changed";
  }

  showAddSkill(){
    this.addLinkClicked = true;
  }


}
