import { Component } from '@angular/core';
import { Sede } from '../Model/Sede';
import { APIService } from '../Services/api.service';

@Component({
  selector: 'app-sede',
  templateUrl: './sede.component.html',
  styleUrls: ['./sede.component.css']
})
export class SedeComponent {
  listaSedes: Sede[] = [];
  sedeByID: Sede = new Sede;
  sedeCrear: Sede = new Sede;
  sedeModificar: Sede = new Sede;

  idBuscar: number = 0;
  idBorrar: number = 0;

  constructor(private api: APIService) { }

  async getSedes() {
    this.listaSedes = await this.api.getSedes() as Sede[];
    console.log(this.listaSedes)

  }

  async getSedeByID() {
    this.sedeByID = await this.api.getSedeByID(this.idBuscar);

  }

  crearSede() {
    this.api.crearSede(this.sedeCrear);

  }

  modificarSede() {
    this.api.modificarSede(this.sedeModificar);

  }

  borrarSede() {
    this.api.borrarSede(this.idBorrar);
    console.log(this.listaSedes)
  }
}
