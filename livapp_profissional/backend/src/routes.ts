import { Router, Request, Response } from 'express';
import multer from 'multer';

import { isAuthenticated } from './middlewares/isAuthenticated';
//Usuários
import { CreateUserController } from './controllers/user/CreateUserController';
import { AuthUserController } from './controllers/user/AuthUserController';
import { DetailUserController } from './controllers/user/DetailUserController';

//Categorias
import { CreateCategoryController } from './controllers/category/CreateCategoryController';
import { ListCategoryController } from './controllers/category/ListCategoryController';

//Produtos
import { CreateProductController } from './controllers/product/CreateProductController';
import uploadConfig from './config/multer'
import { ListByCategoryController } from './controllers/product/ListByCategoryController';

//Pedidos
import { CreateOrderController } from './controllers/order/CreateOrderController';
import { RemoveOrderController } from './controllers/order/RemoveOrderController';
import { AddItemController } from './controllers/order/AddItemController';
import { RemoveItemController } from './controllers/order/RemoveItemController';
import { SendOrderController } from './controllers/order/SendOrderController';
import { ListOrderController } from './controllers/order/ListOrderController';
import { DetailsOrdersController } from './controllers/order/DetailsOrdersController';
import { FinishOrderController } from './controllers/order/FinishOrderController';


import { ListPerformanceController } from './controllers/performance/ListPerformanceController';


const router = Router();
const upload = multer(uploadConfig.upload("./tmp"))

//Rotas de Usuário
router.post('/users', new CreateUserController().handle)
router.post('/session', new AuthUserController().handle)
router.get('/me', isAuthenticated, new DetailUserController().handle)

//Rotas de Categoria
router.post('/category', isAuthenticated, new CreateCategoryController().handle)
router.get('/listcategory', isAuthenticated, new ListCategoryController().handle)

//Rotas de Produto
router.post('/product', isAuthenticated, upload.single('file'), new CreateProductController().handle)
router.get('/category/product', isAuthenticated, new ListByCategoryController().handle)

//Rotas de Pedidos
router.post('/order', isAuthenticated, new CreateOrderController().handle)
router.delete('/order', isAuthenticated, new RemoveOrderController().handle)
router.post('/order/add', isAuthenticated, new AddItemController().handle)
router.delete('/order/remove', isAuthenticated, new RemoveItemController().handle)
router.put('/order/send', isAuthenticated, new SendOrderController().handle)
router.get('/orders', isAuthenticated, new ListOrderController().handle)
router.get('/order/detail', isAuthenticated, new DetailsOrdersController().handle)
router.put('/order/finish', isAuthenticated, new FinishOrderController().handle)

//Rotas de Performance
router.get('/performance', isAuthenticated, new ListPerformanceController().handle)
export { router };