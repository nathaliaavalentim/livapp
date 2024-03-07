import { Header } from '../../components/Header'
import styles from './styles.module.scss'
import Head from 'next/head'
import { canSSRAuth } from '../../utils/canSSRAuth'
import { FiUpload } from 'react-icons/fi'
import { ChangeEvent, FormEvent, useState } from 'react'
import { setupAPIClient } from '../../services/api'
import { toast } from 'react-toastify'

type ProductProps = {
    id: string;
    name: string;
}

interface ProdProps {
    productList: ProductProps[];
}


export default function Order({ productList }: ProdProps) {

    const [dateSession, setDateSession] = useState('');
    const [products, setProducts] = useState(productList || []);
    const [productSelected, setProductSelected] = useState(0);
    const [schedule, setSchedule] = useState('');




    //Quando seleciona uma nova categoria na lista
    function handleChangeProduct(e) {
        setProductSelected(e.target.value)
    }


    //Registrando o produto
    async function handleRegister(e: FormEvent) {
        e.preventDefault();
        try {
            const apiClient = setupAPIClient();
            await apiClient.post('/order', {
                'name_product': products[productSelected].name,
                'product_id': products[productSelected].id,
                'dateSession': dateSession,
                'schedule': schedule

            });
            toast.success("Sessão agendada com sucesso.")

        }
        catch (err) {
            toast.error("Ops! Erro ao agendar.")
        }

        setProducts([]);
        setDateSession('');
        window.location.href ="/dashboard"


    }



    return (
        <>
            <Head>
                <title>Nova Sessão</title>
            </Head>
            <div>
                <Header />

                <main className={styles.container}>
                    <h1>Nova Sessão</h1>


                    <form className={styles.form} onSubmit={handleRegister}>



                        <select value={productSelected} onChange={handleChangeProduct} placeholder='Nome do Aluno'>
                            {products.map((item, index) => {
                                return (
                                    <option key={item.id} value={index}>
                                        {item.name}
                                    </option>
                                )
                            })}

                        </select>



                        <input
                            type='date'
                            placeholder='Data da Sessão'
                            className={styles.input}
                            value={dateSession}
                            onChange={(e) => setDateSession(e.target.value)}
                        />

<input
                            type='time'
                            placeholder='Hora da Sessão'
                            className={styles.input}
                            value={schedule}
                            onChange={(e) => setSchedule(e.target.value)}
                        />






                        <button className={styles.buttonAdd} type='submit'>Cadastrar</button>

                    </form>

                </main>
            </div>



        </>

    )
}

export const getServerSideProps = canSSRAuth(async (context) => {

    const apiClient = setupAPIClient(context);

    const response = await apiClient.get('/category/product')


    return {
        props: {
            productList: response.data
        }
    }
})