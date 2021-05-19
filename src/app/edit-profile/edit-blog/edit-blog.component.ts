import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-blog',
  templateUrl: './edit-blog.component.html',
  styleUrls: ['./edit-blog.component.scss']
})
export class EditBlogComponent implements OnInit {
  blogLinks = []
  addLinkClicked:boolean = false;
  constructor() { }

  ngOnInit(): void {
  }

  showAddBlog(){
    this.addLinkClicked = true;
  }

  removeBlog() {
    //
  }

}
