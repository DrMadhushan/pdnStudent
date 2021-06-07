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
  isWrongCredential:boolean = false;

  constructor(private auth: AngularFireAuth, public router:Router){  }

  getCurrentUser(){
    const user = firebase.auth().currentUser;
    if(user !== null){
      return user.uid;
    }
    return "guest";
  }

  async signIn(email:string, password:string){

    this.auth.signInWithEmailAndPassword(email, password)
    .catch(error => {
      if(error.code == 'auth/wrong-password'){
        window.alert("Wrong password!");
      }
      else if(error.code == 'auth/network-request-failed'){
        window.alert("Check your internet connection!");
      }
      else if(error.code == 'auth/user-not-found'){
        window.alert("User not found!\nPlease check your email");
      }
      else if(error.code = 'auth/invalid-email'){
        window.alert("Invalid email!");
      }
      else{
        window.alert("Some unexpected error occured!\nPlease refresh the tab and try again");
      }
      console.log(error.message);
      console.log(error.code);
      this.router.navigate(['signin'])
    }).then(userCredentials => {
      localStorage.setItem('user',this.getCurrentUser());
    });
  
    this.isSignedIn = true; 
    localStorage.setItem('user', this.getCurrentUser());
    console.log("Current user: "+localStorage.getItem('user'));

    if (localStorage.getItem('user') !="guest"){
      this.router.navigate(['edit-profile']);
      return null;
    }
    this.isWrongCredential = true;
    return null;

  }

  logout(){
    if(localStorage.getItem('user') != 'guest'){
      this.auth.signOut();
      localStorage.setItem('user','guest');
    }
    this.router.navigate(['home']);
    
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

    // const user = localStorage.getItem('user');
    // const jsonTree = JSON.parse(usrStr);
    // console.log("My json is = "+jsonTree);
    // //console.log("Current user is: " + user);
    // let keys = Object.keys(jsonTree);
    // keys.forEach( function(key) {
    //   var values = jsonTree[key]
    //   console.log(values+"---->")
    //   // do stuff with "values"
    // })