import Modal from 'react-modal';
import styles from './styles.module.scss';
import { FiX } from 'react-icons/fi';
import { Chart } from "react-google-charts";
import React from 'react';
import faker from 'faker';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);



interface ModalChartProps{
  isOpen: boolean;
  onRequestClose: () => void;
  dataPerformance: []
}



export function ModalChart({ isOpen, onRequestClose, dataPerformance}: ModalChartProps){

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

  const options = {
    responsive: true,
    plugins: {
        legend: {
            position: 'top' as const,
        },
        title: {
            display: false,
            text: 'Dataset',
        },
    },
};

let labels = [];
let values = [];
for(let i=0;i<dataPerformance.length;i++){
  let instance = dataPerformance[i];
  labels.push(String(instance['date']).substring(0,10));
  values.push(parseFloat(instance['des']));
}

const data = {
    labels,
    datasets: [
        {
          label: 'Desempenho por Sessão',
          data: values,
          borderColor: 'rgb(255, 99, 132)',
          backgroundColor: 'rgba(255, 99, 132, 0.5)',
          //borderWidth: 1
        },
    ],
};

console.log("ESTOU AQUIIIII")
console.log(dataPerformance)

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

      <h2>Gráfico de Desempenho:</h2>
      <Line options={options} data={data} />
    </div>

   </Modal>
  )
}