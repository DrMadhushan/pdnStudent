import { AuthService } from './../shared/services/auth.service';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AngularFireAuth } from '@angular/fire/auth';
// import { firebase } from '@angular/fire/';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.scss']
})
export class SigninComponent implements OnInit {
  isSignedIn:boolean = false;
  // constructor(public auth: AngularFireAuth, public router: Router) { }
  constructor (public authService: AuthService, public router: Router){}
  ngOnInit(): void {
    if(localStorage.getItem('user') !== null){
      this.isSignedIn = true;
    }
  }

  async onSignin(email:string, password:string){
    await this.authService.signIn(email,password);
    if(this.authService.isSignedIn){
      this.isSignedIn = true;
    }
  }

  

  /*
  onSignin(email:string, password:string){
    console.log(email," ",password);
    this.auth.signInWithEmailAndPassword(email,password)
    .catch(error => console.log(error.code))
    .then(res => console.log(res));

    this.isSignedIn = true
    this.router.navigate(['edit-profile'])
  }*/

}
