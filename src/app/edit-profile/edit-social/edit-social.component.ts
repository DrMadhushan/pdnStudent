import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-social',
  templateUrl: './edit-social.component.html',
  styleUrls: ['./edit-social.component.scss']
})
export class EditSocialComponent implements OnInit {
  socialAccounts = [["facebook","fblink"],["instagram","instalink"],["twitter","twitterlink"]]
  available_social_media = ["Facebook", "Twitter", "Instagram", "Github", "StackOverFlow", "LinkedIn", "Hackerrank"]
  addLinkClicked:boolean = false;

  constructor() { }

  ngOnInit(): void {
  }

  removeLink(){
    // method to remove social link from database
  }

  showAddLink(){
    this.addLinkClicked = true;
  }

  addLink(){
    // method to remove social link from database
  }
  
}
