import { Component } from '@angular/core';
import { APIService } from '../Services/api.service';
import { Pedido } from '../Model/pedido';


@Component({
  selector: 'app-operario',
  templateUrl: './pedido.component.html',
  styleUrls: ['./pedido.component.css']
})


export class PedidoComponent {

  listaPedidos: Pedido[] = [];
  pedidoByID: Pedido = new Pedido;
  pedidoCrear: Pedido = new Pedido;
  pedidoModificar: Pedido = new Pedido;

  idBuscar: number = 0;
  idBorrar: number = 0;

  constructor(private api: APIService) { }

  async getPedidos() {
    this.listaPedidos = await this.api.getListaPedidos();

  }

  async getPedidoPorID() {
    this.pedidoByID = await this.api.getPedidoPorID(this.idBuscar);

  }

  crearPedido() {
    this.api.crearPedido(this.pedidoCrear);

  }

  modificarPedido() {
    this.api.modificarPedido(this.pedidoModificar);

  }

  borrarPedido() {
    this.api.borrarPedido(this.idBorrar);

  }

}
