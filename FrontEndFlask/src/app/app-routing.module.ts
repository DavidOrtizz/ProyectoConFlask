import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { OperarioComponent } from './operario/operario.component';
import { ProductoComponent } from './producto/producto.component';
import { SedeComponent } from './sede/sede.component';
import { PedidoComponent } from './pedido/pedido.component';
import { LandingComponent } from './landing/landing.component';

const routes: Routes = [
  { path: '', component: LandingComponent },
  { path: 'operario', component: OperarioComponent },
  { path: 'producto', component: ProductoComponent },
  { path: 'productos', component: ProductoComponent },
  { path: 'sede', component: SedeComponent },
  { path: 'pedido', component: PedidoComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
