import { Component } from '@angular/core';
import { APIService } from '../Services/api.service';
import { Operario } from '../Model/operario';

@Component({
  selector: 'app-operario',
  templateUrl: './operario.component.html',
  styleUrls: ['./operario.component.css']
})
export class OperarioComponent {

  listaOperarios: Operario[] = [];
  operarioByID: Operario = new Operario;
  operarioCrear: Operario = new Operario;
  operarioModificar: Operario = new Operario;

  idBuscar: number = 0;
  idBorrar: number = 0;

  constructor(private api: APIService) { }

  async getOperarios() {
    this.listaOperarios = await this.api.getOperarios();

  }

  async getOperarioByID() {
    this.operarioByID = await this.api.getOperarioByID(this.idBuscar);

  }

  crearOperario() {
    this.api.crearOperario(this.operarioCrear);

  }

  modificarOperario() {
    this.api.modificarOperario(this.operarioModificar);

  }

  borrarOperario() {
    this.api.borrarOperario(this.idBorrar);

  }

}
