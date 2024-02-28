import { canSSRAuth } from "../../utils/canSSRAuth"
import Head from "next/head"
import { Header }  from "../../components/Header"
import style from "./styles.module.scss";
import { FiRefreshCcw } from "react-icons/fi";
import { setupAPIClient } from "../../services/api";
import { useState } from "react";
import Modal from 'react-modal';
import { ModalOrder } from "../../components/ModalOrder";
import  Link  from 'next/link'
import { useHref } from "react-router-dom";


type OrdemProps = {
    id: string;
    table: string | number;
    status: boolean;
    draft: boolean;
    name: string | null;
    date: string;
    time: string;
}
interface HomeProps{
    orders: OrdemProps[];
}

export type OrderItemProps = {
    id: string;
	amount: number;
    order_id: string;
    product_id: string;
    products:{
        id: string;
        name: string;
        description: string;
        price: string;
        banner: string;
        date: string;
        time: string;
    }
    orders:{
        id: string;
        table: string | number;
        status: string;
        name: string | null;
        date: string;
        time: string;
        }
}


export default function Dashboard({orders}: HomeProps) {

    const [orderList, setOrderList] = useState(orders || [])
    const [modalItem, setModalItem] = useState<OrderItemProps[]>();
    const [modalVisible, setModalVisible] = useState(false);

    //Fechar o Modal
    function closeModal(){
        setModalVisible(false);
    }


    async function handleCreateOrder() {
        window.location.href = 'order/' 
    }




    //Mostrar os detalhes doe um atendimento no Modal
    async function handleModal(id: string){
        const apiClient = new setupAPIClient();
        const response = await apiClient.get('/order/detail', {
            param:{
                order_id: id
            }
        })
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

    //Vindo do react-modal
    Modal.setAppElement('#__next')

    return (
        <>
        <Head>
            <title>Atendimento</title>
        </Head>

        <div>
            <Header/>
            <main className={style.container}>
                <div className={style.containerHeader}>
                    <h1> Sessões Agendadas </h1>
                    <button onClick={handleRefreshOrders} className={style.button}><FiRefreshCcw size={25} color="red"/></button>
                </div>

                <article className={style.listOrders}>

                    {orderList.length  === 0 && (
                        <span className={style.emptyList}>Nenhuma sessão agendada.</span>
                    )}


                        {orderList.map(item => (
                            <section key={item.id} className={style.orderItem}>
                                <button onClick={()=> handleModal(item.id)}className={style.button2}>
                                    <div className={style.tag}>
                                    <span>Nome: {item.name} | Data: {item.date} | Horário: {item.time}
                                     </span>
                                     </div>
                                </button>
                            </section>
                    ))}

                </article>

               
                            <button type="submit" onClick={handleCreateOrder} className={style.buttonAdd}>
                                Nova Sessão
                            </button>

                        
            </main>

            {modalVisible && (
                <ModalOrder
                    isOpen={modalVisible}
                    onRequestClose={closeModal}
                    orders={modalItem}
                    handleFinishOrder={handleFinishItem}/>
            )}
        </div>

        </>

    )
}

export const getServerSideProps = canSSRAuth(async (context) => {
    const apiClient = setupAPIClient(context);
    const response = await apiClient.get('/order/detail');

    console.log(response.data)
    return {
        props: {
            orders: response.data
        }
    }
})