import { FormEvent, useEffect, useState } from "react";
import Head from "next/head";
import { Header } from "../../components/Header";
import style from "./styles.module.scss";
import { setupAPIClient } from "../../services/api";
import { toast } from "react-toastify";
import { canSSRAuth } from "../../utils/canSSRAuth";


type ItemProps = {
    id: string;
    name: string;
    date: string;
    time: string;
}
interface ProductProps {
    productList: ItemProps[];
}

export default function Order({ productList }: ProductProps) {

    const [name, setName] = useState(productList);
    const [productSelected, setProductSelected] = useState(0);
    const [date, setDate] = useState('');
    const [time, setTime] = useState('');

    function handleChangeProduct(e) {
        setProductSelected(e.target.value)
    }

    async function handleRegister(e: FormEvent) {
        e.preventDefault();
    
        try {
            if (name.length === 0) {
                return; // Evitar a submissão se não houver itens selecionados
            }

            console.log(name[productSelected].name)
            console.log(date)
            console.log(time)
    

            const data = JSON.stringify({
                name: name[productSelected].name,
                date: date,
                time: time
            });

        console.log('Dados:'+data)
        
    
            const apiClient = setupAPIClient(undefined);
            await apiClient.post('/order', data);
            toast.success("Sessão cadastrada com sucesso.");
        } catch (err) {
            toast.error("Ops! Erro ao cadastrar.");
        }
    }

    
    return (
        <>
            <Head><title>Nova Sessão</title></Head>
            <div>
                <Header />
                <main className={style.container}>
                    <h1>Nova Sessão</h1>
                    <form className={style.form} onSubmit={handleRegister}>
                    
                    <select className={style.select} value={productSelected} onChange={handleChangeProduct}>
                            {name && name.map((item, index) => {
                                return (
                                    <option key={item.id} value={index}>
                                        {item.name}
                                    </option>
                                )
                            })}
                        </select>
                        <input
                            type="date"
                            placeholder="Data"
                            className={style.input}
                            value={date}
                            onChange={(e) => setDate(e.target.value)}

                        />


                        <input
                            
                            placeholder="Horário"
                            className={style.input}
                            value={time}
                            onChange={(e) => setTime(e.target.value)}

                        />


                        <button type="submit" className={style.buttonAdd}>
                            Cadastrar
                        </button>

                    </form>

                </main>
            </div>
        </>
    )
}

export const getServerSideProps = canSSRAuth(async (context) => {
    
    const apiClient = setupAPIClient(context);

    const response = await apiClient.get('/category/product')
    console.log(JSON.stringify(response.data));


    return {
        props: {
            productList: response.data
        }
    }
})