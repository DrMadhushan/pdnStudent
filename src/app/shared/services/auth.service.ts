import { Injectable } from '@angular/core';
import { AngularFireAuth } from "@angular/fire/auth";
import firebase from "firebase/app";
import "firebase/auth";
import { AngularFirestore, AngularFirestoreDocument } from '@angular/fire/firestore';
import { Router } from "@angular/router";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  isSignedIn:boolean = false;
  constructor(private auth: AngularFireAuth, public router:Router){  }

  async signIn(email:string, password:string){
    this.auth.signInWithEmailAndPassword(email, password)
    .catch(error => console.log(error.code))
    .then(res => {
      this.isSignedIn = true; 
      console.log(res);
      localStorage.setItem('user',JSON.stringify(res));
      this.router.navigate(['edit-profile'])
    });

  }

  logout(){
    if(localStorage.getItem('user') != null)
    this.auth.signOut();
    localStorage.removeItem('user');
  }

  sendResetPasswordEmail(email:any){
    if(email != null){
      firebase.auth().sendPasswordResetEmail(email)
      .catch(function(error){
        console.log(error.message);
      });
      window.alert("Reset password email has been sent to your email.\nPlease check and follow the instructions.");
    }
  }
}
