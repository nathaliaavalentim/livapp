import { Request, Response } from "express";
import { ListPerformanceService } from "../../services/performance/ListPerformanceService";


class ListPerformanceController{
    async handle(req: Request, res: Response){

        //get com parametros: req.query
        //req.query contém os parâmetros de consulta da solicitação
        const aluno_id = req.query.aluno_id as string;
        
        
        const listPerformance = new ListPerformanceService();

        const performance = await listPerformance.execute({
            aluno_id
        });
        return res.json(performance);
    }

}

export{ListPerformanceController}