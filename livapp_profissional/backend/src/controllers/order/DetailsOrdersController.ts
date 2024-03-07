import { Request, Response } from "express";
import { DetailsOrdersService} from "../../services/order/DetailsOrdersService";

class DetailsOrdersController{
    async handle(req: Request, res: Response){
        //get com parametros: req.query
        //req.query contém os parâmetros de consulta da solicitação.

        console.log(req.query)

        const order_id = req.query.order_id as string;

        console.log(order_id)

        const detailsOrdersService = new DetailsOrdersService();

        const orders = await detailsOrdersService.execute({
            order_id
        })

        console.log(orders)

        return res.json(orders)
    }

}

export {DetailsOrdersController}