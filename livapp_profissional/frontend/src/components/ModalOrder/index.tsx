import Modal from 'react-modal';
import styles from './styles.module.scss';

import { FiX } from 'react-icons/fi';
import { ModalGraph } from "../../components/ModalGraph";
import { OrderItemProps } from '../../pages/dashboard'
import { useState } from 'react';

interface ModalOrderProps{
  isOpen: boolean;
  onRequestClose: () => void;
  orders: OrderItemProps[];
  handleFinishOrder: (id: string) => void;
}

export function ModalOrder({ isOpen, onRequestClose, orders, handleFinishOrder  }: ModalOrderProps){

  
  const [modalItem, setModalItem] = useState<OrderItemProps[]>();
  const [modalVisible, setModalVisible] = useState(false);

  async function handleModal(){
    setModalVisible(true);
}

  //Fechar o Modal
  function closeModal(){
      setModalVisible(false);
  }


  const customStyles = {
    content:{
      top: '50%',
      bottom: 'auto',
      left: '50%',
      right: 'auto',
      padding: '30px',
      transform: 'translate(-50%, -50%)',
      backgroundColor: '#1d1d2e'
    }
  };

  //Vindo do react-modal
  //Modal.setAppElement('#__next')


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

      <h2>Detalhes do atendimento</h2>

      
      {orders.map( item => (
        <section key={item.id} className={styles.containerItem}>
          <span>{item.amount} - <strong>{item.products.name}</strong></span>
          <span className={styles.description}>
            {item.products.description}
          </span>
        </section>
      ))}


      <button className={styles.buttonOrder} onClick={ () => handleFinishOrder(orders[0].order_id) }>
        Concluir Atendimento
      </button><p></p>

      <button className={styles.buttonOrder} onClick={ () => handleModal() }>
        Gráfico de Desempenho
      </button>

      {modalVisible && (
                <ModalGraph
                    isOpen={modalVisible}
                    onRequestClose={closeModal}
                    />
            )}


    </div>

   </Modal>
  )
}