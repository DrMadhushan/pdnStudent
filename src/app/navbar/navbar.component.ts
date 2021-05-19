import { AuthService } from './../shared/services/auth.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'nav-bar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  isLoggedIn:boolean = false;
  constructor(public authService: AuthService) { }

  ngOnInit(): void {
    if(localStorage.getItem('user') != null){
      this.isLoggedIn = true;
    }
  }

  logout(){
    this.authService.logout();
  }

}
