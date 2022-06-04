<script>
	import Header from './componentes/Header.svelte'
	import Nav from './componentes/Nav.svelte'
	import Section01 from './componentes/Section01.svelte'
	import Section02 from './componentes/Section02.svelte'
	import Section03 from './componentes/Section03.svelte'
	import Section04 from './componentes/Section04.svelte'
	import Footer from './componentes/Footer.svelte'
</script>


<main>
	<Header />
	<Nav />
	<Section01 />
	<!-- <Section02 /> -->
	<!-- <Section03 /> -->
	<Section04 />
	<!-- <Footer /> -->
</main>

<style>
main {
	text-align: center;
	padding: 1em;
	max-width: 600px;
	margin: 0 auto;
}

@media (min-width: 640px) {
	main {
		max-width: none;
	}
}
</style>

