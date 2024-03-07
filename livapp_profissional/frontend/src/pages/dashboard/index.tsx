import { canSSRAuth } from "../../utils/canSSRAuth"
import Head from "next/head"
import { Header }  from "../../components/Header"
import styles from "./styles.module.scss";
import { FiRefreshCcw } from "react-icons/fi";
import { setupAPIClient } from "../../services/api";
import { useState } from "react";
import Modal from 'react-modal';
import { ModalOrder } from "../../components/ModalOrder";
import { redirect } from "next/dist/server/api-utils";


type OrdemProps = {
    id: string;
    table: string | number;
    status: boolean;
    draft: boolean;
    name: string | null;
    name_product: string;
    dateSession: string;
    description: string;
    schedule: string;
    product_id: number;
}
interface HomeProps{
    orders: OrdemProps[];
}

export type OrderItemProps = {
    id: string;
	amount: number;
    order_id: string;
    product_id: string;
    name_product: string;
    dateSession: string;
    description: string;
    schedule: string;
    products:{
        id: string;
        name: string;
        description: string;
        price: string;
        banner: string;
    }
    orders:{
        id: string;
        table: string | number;
        status: string;
        name: string | null;
        created_at: Date;
        dateSession: string;
        name_product: string;
        product_id: string;
        }
}


export default function Dashboard({orders}: HomeProps) {

    const [orderList, setOrderList] = useState(orders || [])
    const [modalItem, setModalItem] = useState<OrderItemProps[]>();
    const [modalVisible, setModalVisible] = useState(false);
    const [dataPerformance, setDataPerformance] = useState([])

    //Fechar o Modal
    function closeModal(){
        setModalVisible(false);
    }




    //Mostrar os detalhes doe um atendimento no Modal
    async function handleModal(id: string, aluno_id: number){
        const apiClient = new setupAPIClient();
        console.log(aluno_id);
        const response = await apiClient.get('/order/detail?order_id='+id, {
            param:{
                order_id: id
            }
        })

        const response2 = await apiClient.get('/performance?aluno_id='+aluno_id, {
            param:{
                aluno_id: id
            }
        })

        console.log(response2);

        setDataPerformance(response2.data)
        setModalItem(response.data);
        setModalVisible(true);
        
    }




    //Concluir o atendimento na tela, atualizando os dados do dashboard:
    async function handleFinishItem(id: string){
        const apiClient = setupAPIClient();
        await apiClient.put('/order/finish', {
            order_id: id,
        })
        const response = await apiClient.get('/orders');
        setOrderList(response.data);
        setModalVisible(false);
    }

    //Refresh no Dashboard
    async function handleRefreshOrders(){
        const apiClient = setupAPIClient();
        const response = await apiClient.get('/orders')
        setOrderList(response.data);

    }



    async function handleNewOrders(){
        window.location.href ="/order"
    }

    //Vindo do react-modal
    Modal.setAppElement('#__next')

    return (
        <>
        <Head>
            <title>Atendimento</title>
        </Head>

        <div>
            <Header/>
            <main className={styles.container}>
                <div className={styles.containerHeader}>
                    <h1> Sessões Agendadas </h1>
                    <button onClick={handleRefreshOrders} className={styles.button}><FiRefreshCcw size={25} color="red"/></button>
                </div>

                <article className={styles.listOrders}>

                    {orderList.length  === 0 && (
                        <span className={styles.emptyList}>Nenhum atendimento em aberto.</span>
                    )}


                        {orderList.map(item => (
                            <section key={item.id} className={styles.orderItem}>
                                <button onClick={()=> handleModal(item.id, item.product_id)}className={styles.button}>
                                    <div className={styles.tag}></div>
                                    <span>
                                        Aluno(a): {item.name_product}    -----   
                                    </span> <br/>
                                    <span>
                                         ----- Data:  {item.dateSession}  -----   
                                    </span><br/>
                                    <span>
                                      ----- Horário: {item.schedule}    
                                    </span><br/>
                                </button>
                            </section>
                    ))}

                </article>

                <button onClick={handleNewOrders} type="submit" className={styles.buttonAdd}>
                                Nova Sessão 
                            </button>
            </main>

            {modalVisible && (
                <ModalOrder
                    isOpen={modalVisible}
                    onRequestClose={closeModal}
                    orders={modalItem}
                    handleFinishOrder={handleFinishItem}
                    dataPerformance={dataPerformance}/>
            )}
        </div>



        </>

    )
}

export const getServerSideProps = canSSRAuth(async (context) => {
    const apiClient = setupAPIClient(context);
    const response = await apiClient.get('/orders');

    console.log(response.data)
    return {
        props: {
            orders: response.data
        }
    }
})