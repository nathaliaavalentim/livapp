import prismaClient from "../../prisma";

interface PerformanceRequest{
    aluno_id: string
}

class ListPerformanceService{
    async execute({aluno_id}: PerformanceRequest){

        const findPerformance = await prismaClient.performance.findMany({
            where:{
                aluno_id: aluno_id
            }
        })
        return findPerformance;
    }
}

export {ListPerformanceService}