<script>
	import Header from './componentes/Header.svelte'
	import Nav from './componentes/Nav.svelte'
	import Main from './componentes/Main.svelte'
	import Footer from './componentes/Footer.svelte'
</script>


<main>
	<Header />
	<Nav />
	<Main />
	<Footer />
</main>

<style>
main {
	text-align: center;
	padding: 1em;
	max-width: 240px;
	margin: 0 auto;
}

@media (min-width: 640px) {
	main {
		max-width: none;
	}
}
</style>

