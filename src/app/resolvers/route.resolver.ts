import { DatabaseService } from './../shared/services/database.service';
import { Injectable } from "@angular/core";
import { forkJoin, of } from "rxjs";
import { Resolve } from "@angular/router";

@Injectable()
export class RouteResolver implements Resolve<any>{
    constructor(private databaseService: DatabaseService){

    }

    resolve(){
        console.log("Route resolve")
        return this.databaseService.getUserViewData();
    }
}