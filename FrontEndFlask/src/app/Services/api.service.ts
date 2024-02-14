import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import * as config from '../../assets/config.json';
import { lastValueFrom } from 'rxjs';
import { Operario } from '../Model/operario';

@Injectable({
  providedIn: 'root'
})
export class APIService {

  private config: any = config;
  private url: string = '';

  constructor(private http: HttpClient) {
    this.url = this.config.api.host;
  }

  // Peticiones OPERARIO
  // Con el rol Usuario
  async getOperarios() {
    const request$ = await this.http.get(this.url + "/operario");
    let listaOperarios: Operario[] = await lastValueFrom(request$) as Operario[]
    return listaOperarios;
  }

  // Operario por ID
  async getOperarioByID(id: number) {
    const request$ = await this.http.get(this.url + "/operario/" + id);
    let operario: Operario = await lastValueFrom(request$) as Operario
    return operario;
  }

  // Crear Operario
  async crearOperario(operario: Operario) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.post(this.url + "/operario", JSON.stringify(operario), options);
    await lastValueFrom(request$)
  }

  // Modificar Operario
  async modificarOperario(operario: Operario) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.put(this.url + "/operario/" + operario.ID, JSON.stringify(operario), options);
    await lastValueFrom(request$)
  }

  // Borrar Operario
  async borrarOperario(id: number) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.delete(this.url + "/operario/" + id, options);
    await lastValueFrom(request$)
  }

}
