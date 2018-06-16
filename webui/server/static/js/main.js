async function api(url, opts = {}) {
    opts.credentials = opts.credentials || 'include'
    const resp = await fetch(url, opts)
    const dat = await resp.json()
    if (dat.status === 'ok') {
        return dat.data
    } else {
        throw new Error(dat.status)
    }
}

var challmodal = new Vue({
    el: '#project-modal',
    data: {
        newProject: {
            name: '',
            target: '',
            desc: '',
        }
    },
    methods: {
        add() {
            let formData = new FormData()
            formData.append("name", this.newProject.name)
            formData.append("target", this.newProject.target)
            formData.append("desc", this.newProject.desc)
            api('project', {
                method: "POST",
                body: formData
            })
            $('#project-modal').modal('hide')
        }
    }
})
