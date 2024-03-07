import Modal from 'react-modal';
import styles from './styles.module.scss';
import InputMask from "react-input-mask";
import { useState } from "react";
import { ModalChart } from "../ModalChart"

import { FiX } from 'react-icons/fi'

import { OrderItemProps } from '../../pages/dashboard'

interface ModalOrderProps{
  isOpen: boolean;
  onRequestClose: () => void;
  orders: OrderItemProps[];
  handleFinishOrder: (id: string) => void;
  dataPerformance: [];
}


export function ModalOrder({ isOpen, onRequestClose, orders, handleFinishOrder, dataPerformance }: ModalOrderProps) {
  const [orderList, setOrderList] = useState(orders || [])
  const [modalItem, setModalItem] = useState<OrderItemProps[]>();
  const [modalVisible, setModalVisible] = useState(false);
  console.log(orders)

  const customStyles = {
    content: {
      top: '50%',
      bottom: 'auto',
      left: '50%',
      right: 'auto',
      padding: '30px',
      transform: 'translate(-50%, -50%)',
      backgroundColor: '#1d1d2e'
    }
  };

  function handleChart() {
    alert("Aqui está seu gráfico.")
  }

  //Fechar o Modal
  function closeModal() {
    setModalVisible(false);
  }

   //Mostrar os detalhes de um atendimento no Modal
   async function handleModal(){
    setModalVisible(true);
}
    //Vindo do react-modal
    Modal.setAppElement('#__next')


  return(
   <Modal
    isOpen={isOpen}
    onRequestClose={onRequestClose}
    style={customStyles}
   >

    <button
    type="button"
    onClick={onRequestClose}
    className="react-modal-close"
    style={{ background: 'transparent', border:0 }}
    >
      <FiX size={45} color="#f34748" />
    </button>

    <div className={styles.container}>

      <h2>Detalhes da Sessão</h2><br/>
      <span className={styles.table}>
        <strong>{orders[0].name_product}</strong><br/>
      </span><br/><br/>
      <span>
        Data da Sessão: {orders[0].dateSession}
      </span><br/><br/>
      <span>
        Horário da Sessão: {orders[0].schedule}
      </span><br/><br/>

     

    


      <button className={styles.buttonOrder} onClick={ () => handleFinishOrder(orders[0].id) }>
        Concluir Atendimento
      </button>

      <button className={styles.buttonOrder} onClick={ () => handleModal() }>
        Acessar Gráfico
      </button>



    </div>
    <div>
    {modalVisible && (
                <ModalChart
                    isOpen={modalVisible}
                    onRequestClose={closeModal}
                    dataPerformance={dataPerformance}/>
            )}
    </div>

   </Modal>
  )
}