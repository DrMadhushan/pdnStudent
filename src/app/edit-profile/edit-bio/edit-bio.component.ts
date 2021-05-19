import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-bio',
  templateUrl: './edit-bio.component.html',
  styleUrls: ['./edit-bio.component.scss']
})
export class EditBioComponent implements OnInit {
  userBio:string = `Lorem ipsum dolor sit amet, ei purto tamquam ceteros his, 
                    eos in graece posidonium. Ex nullam vidisse salutatus
                    sed, ea persius phaedrum.
                    `
  editBio:boolean = false;
  constructor() { }

  ngOnInit(): void {
  }

  showEditBio(){
    this.editBio = true;
  }

}
