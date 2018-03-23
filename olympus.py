# -*- generated by 1.0.10 -*-
import da
PatternExpr_538 = da.pat.TuplePattern([da.pat.ConstantPattern('Finished Processing'), da.pat.BoundPattern('_BoundPattern541_')])
PatternExpr_560 = da.pat.TuplePattern([da.pat.ConstantPattern('Get Current Config'), da.pat.FreePattern('clientId')])
PatternExpr_567 = da.pat.FreePattern('p')
PatternExpr_806 = da.pat.TuplePattern([da.pat.ConstantPattern('Initialize History Done'), da.pat.BoundPattern('_BoundPattern809_')])
PatternExpr_2315 = da.pat.TuplePattern([da.pat.ConstantPattern('Caught up'), da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern2320_')])
PatternExpr_2407 = da.pat.TuplePattern([da.pat.ConstantPattern('Running state'), da.pat.FreePattern(None)])
PatternExpr_2413 = da.pat.FreePattern('rep')
PatternExpr_2505 = da.pat.TuplePattern([da.pat.ConstantPattern('Get Config'), da.pat.FreePattern('clientid')])
PatternExpr_2512 = da.pat.FreePattern('p')
PatternExpr_2537 = da.pat.TuplePattern([da.pat.ConstantPattern('Reconfiguration request from replica'), da.pat.FreePattern('replica')])
PatternExpr_2544 = da.pat.FreePattern('p')
PatternExpr_2586 = da.pat.TuplePattern([da.pat.ConstantPattern('Reconfiguration request from client'), da.pat.FreePattern('client_result'), da.pat.FreePattern('result'), da.pat.FreePattern('result_proof'), da.pat.FreePattern('client')])
PatternExpr_2599 = da.pat.FreePattern('p')
PatternExpr_2641 = da.pat.TuplePattern([da.pat.ConstantPattern('Wedge response'), da.pat.FreePattern('wedgedMessage'), da.pat.FreePattern('replica')])
PatternExpr_2650 = da.pat.FreePattern('p')
PatternExpr_2703 = da.pat.TuplePattern([da.pat.ConstantPattern('Caught up'), da.pat.FreePattern('state_hash'), da.pat.FreePattern('lastresultstatements'), da.pat.FreePattern('replica')])
PatternExpr_2714 = da.pat.FreePattern('p')
PatternExpr_2734 = da.pat.TuplePattern([da.pat.ConstantPattern('Running state'), da.pat.FreePattern('running_state')])
PatternExpr_2741 = da.pat.FreePattern('p')
_config_object = {'channel': {'fifo', 'reliable'}, 'clock': 'lamport'}
import sys
import os
import time
import random
import datetime
import string
import itertools
from utils import Utils, State
CLIENT = da.import_da('client')
REPLICA = da.import_da('replica')

class Olympus(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._OlympusReceivedEvent_0 = []
        self._OlympusReceivedEvent_2 = []
        self._OlympusReceivedEvent_3 = []
        self._OlympusReceivedEvent_4 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_0', PatternExpr_538, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_1', PatternExpr_560, sources=[PatternExpr_567], destinations=None, timestamps=None, record_history=None, handlers=[self._Olympus_handler_559]), da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_2', PatternExpr_806, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_3', PatternExpr_2315, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_4', PatternExpr_2407, sources=[PatternExpr_2413], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_5', PatternExpr_2505, sources=[PatternExpr_2512], destinations=None, timestamps=None, record_history=None, handlers=[self._Olympus_handler_2504]), da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_6', PatternExpr_2537, sources=[PatternExpr_2544], destinations=None, timestamps=None, record_history=None, handlers=[self._Olympus_handler_2536]), da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_7', PatternExpr_2586, sources=[PatternExpr_2599], destinations=None, timestamps=None, record_history=None, handlers=[self._Olympus_handler_2585]), da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_8', PatternExpr_2641, sources=[PatternExpr_2650], destinations=None, timestamps=None, record_history=None, handlers=[self._Olympus_handler_2640]), da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_9', PatternExpr_2703, sources=[PatternExpr_2714], destinations=None, timestamps=None, record_history=None, handlers=[self._Olympus_handler_2702]), da.pat.EventPattern(da.pat.ReceivedEvent, '_OlympusReceivedEvent_10', PatternExpr_2734, sources=[PatternExpr_2741], destinations=None, timestamps=None, record_history=None, handlers=[self._Olympus_handler_2733])])

    def setup(self, olympusPrivateKey, olympusPublicKey, clientPublicKeys, num_replicas, clients, head_timeout, nonhead_timeout, failures, checkpt_interval, **rest_2754):
        super().setup(olympusPrivateKey=olympusPrivateKey, olympusPublicKey=olympusPublicKey, clientPublicKeys=clientPublicKeys, num_replicas=num_replicas, clients=clients, head_timeout=head_timeout, nonhead_timeout=nonhead_timeout, failures=failures, checkpt_interval=checkpt_interval, **rest_2754)
        self._state.olympusPrivateKey = olympusPrivateKey
        self._state.olympusPublicKey = olympusPublicKey
        self._state.clientPublicKeys = clientPublicKeys
        self._state.num_replicas = num_replicas
        self._state.clients = clients
        self._state.head_timeout = head_timeout
        self._state.nonhead_timeout = nonhead_timeout
        self._state.failures = failures
        self._state.checkpt_interval = checkpt_interval
        self._state.olympusPrivateKey = self._state.olympusPrivateKey
        self._state.olympusPublicKey = self._state.olympusPublicKey
        self._state.clientPublicKeys = self._state.clientPublicKeys
        self._state.replicaPrivateKeys = []
        self._state.replicaPublicKeys = []
        self._state.num_replicas = self._state.num_replicas
        self._state.clients = self._state.clients
        self._state.head = None
        self._state.configNo = None
        self._state.failures = self._state.failures
        self._state.head_timeout = self._state.head_timeout
        self._state.nonhead_timeout = self._state.nonhead_timeout
        self._state.tail = None
        self._state.isCurrentConfigValid = False
        self._state.currentState = ''
        self._state.replicas = None
        self._state.possibleQuorumWedges = {}
        self._state.wedgeResponseCount = 0
        self._state.caughtUpResponses = {}
        self._state.utils = Utils()
        self._state.createquorumlock = False
        self._state.replicaToIndexMap = {}
        self._state.indexToReplicaMap = {}
        self._state.checkpt_interval = self._state.checkpt_interval
        self._state.replicarunningstate = None
        self._state.clientIdtoClients = {}
        self._state.checkedquorums = set()

    def run(self):
        self.output((('****Starting Olympus ' + str(self._id)) + '*******'))
        for i in range(0, len(self._state.clients)):
            self._state.clientIdtoClients[('c' + str(i))] = self._state.clients[i]
        self.createNewConfiguration({})
        self.intializeVariables()
        super()._label('_st_label_529', block=False)
        client = None

        def UniversalOpExpr_530():
            nonlocal client
            for client in self._state.clients:

                def ExistentialOpExpr_536(client):
                    for (_, _, (_ConstantPattern552_, _BoundPattern554_)) in self._OlympusReceivedEvent_0:
                        if (_ConstantPattern552_ == 'Finished Processing'):
                            if (_BoundPattern554_ == client):
                                if True:
                                    return True
                    return False
                if (not ExistentialOpExpr_536(client=client)):
                    return False
            return True
        _st_label_529 = 0
        while (_st_label_529 == 0):
            _st_label_529 += 1
            if UniversalOpExpr_530():
                _st_label_529 += 1
            else:
                super()._label('_st_label_529', block=True)
                _st_label_529 -= 1

    def get_failures_for_replica(self, configNo, failures):
        replicaToFailures = {}
        for fkey in failures:
            key = fkey.split(',')
            c = int(key[0])
            r = int(key[1])
            if (c == configNo):
                fkeyList = failures[fkey].split(';')
                replicaToFailures[r] = {}
                for failK in fkeyList:
                    trig = failK[0:failK.rfind(',')].replace(' ', '').strip()
                    fail = failK[(failK.rfind(',') + 1):].replace(' ', '').strip()
                    replicaToFailures[r][trig] = fail
        return replicaToFailures

    def createNewConfiguration(self, runningstate):
        self._state.replicaToIndexMap.clear()
        self._state.indexToReplicaMap.clear()
        self._state.replicaPrivateKeys.clear()
        self._state.replicaPublicKeys.clear()
        self._state.replicas = list(self.new(REPLICA.Replica, num=self._state.num_replicas))
        self._state.head = self._state.replicas[0]
        self._state.tail = self._state.replicas[(- 1)]
        if (self._state.configNo is None):
            self._state.configNo = 0
        else:
            self._state.configNo += 1
        for i in range(0, self._state.num_replicas):
            (replicaPrivateKey, replicaPublicKey) = Utils.getSignedKey(self._id)
            self._state.replicaPrivateKeys.append(replicaPrivateKey)
            self._state.replicaPublicKeys.append(replicaPublicKey)
        replicaFailures = self.get_failures_for_replica(self._state.configNo, self._state.failures)
        for i in range(self._state.num_replicas):
            self._state.replicaToIndexMap[self._state.replicas[i]] = i
            self._state.indexToReplicaMap[i] = self._state.replicas[i]
            replicaFailure = []
            if (i in replicaFailures):
                replicaFailure = replicaFailures[i]
            self._setup(self._state.replicas[i], (self._id, self._state.replicaPublicKeys, self._state.replicaPrivateKeys[i], self._state.olympusPublicKey, State.PENDING.value, self._state.head_timeout, self._state.nonhead_timeout, replicaFailure, self._state.checkpt_interval, runningstate, self._state.clientPublicKeys))
        self._start(self._state.replicas)
        for i in range(self._state.num_replicas):
            self.send(('Become Active', self._state.head, self._state.tail, ('r' + str(i)), self._state.replicas), to=self._state.replicas[i])
        super()._label('_st_label_795', block=False)
        replica = None

        def UniversalOpExpr_796():
            nonlocal replica
            for replica in self._state.replicas:

                def ExistentialOpExpr_804(replica):
                    for (_, _, (_ConstantPattern820_, _BoundPattern822_)) in self._OlympusReceivedEvent_2:
                        if (_ConstantPattern820_ == 'Initialize History Done'):
                            if (_BoundPattern822_ == replica):
                                if True:
                                    return True
                    return False
                if (not ExistentialOpExpr_804(replica=replica)):
                    return False
            return True
        _st_label_795 = 0
        while (_st_label_795 == 0):
            _st_label_795 += 1
            if UniversalOpExpr_796():
                _st_label_795 += 1
            else:
                super()._label('_st_label_795', block=True)
                _st_label_795 -= 1

    def intializeVariables(self):
        self._state.currentState = 'Running'
        self._state.possibleQuorumWedges.clear()
        self._state.caughtUpResponses.clear()
        self._state.checkedquorums.clear()
        self._state.wedgeResponseCount = 0
        self._state.createquorumlock = False
        self._state.replicarunningstate = None
        self._state.isCurrentConfigValid = True

    def check_validity_of_result_proof(self, actual_result, result, result_proof):
        if (not (actual_result == result)):
            return False
        result_statements = result_proof
        for i in range(0, len(self._state.replicas)):
            try:
                statement = self._state.utils.verifySignature(result_statements[i], self._state.replicaPublicKeys[i])
                hash = statement.decode('UTF-8').split(';')[(- 1)]
                if (self._state.utils.verifyHash(result, hash.encode('utf-8')) == False):
                    return False
            except:
                return False
        return True

    def get_so_pair_from_order_statement(self, order_statement):
        strings = order_statement.split(';')
        operation = ((((strings[2] + ';') + strings[3]) + ';') + strings[4])
        slot = int(strings[1])
        return (slot, operation)

    def check_validity_of_history(self, order_proofs):
        slotNos = []
        for i in range(0, len(order_proofs)):
            try:
                if (len(order_proofs[i]) > 0):
                    first_order_statement = self._state.utils.verifySignature(order_proofs[i][0], self._state.replicaPublicKeys[0]).decode('UTF-8')
                    so_pair = self.get_so_pair_from_order_statement(first_order_statement)
                    if (so_pair[0] in slotNos):
                        return False
                    else:
                        slotNos.append(so_pair[0])
                    for j in range(1, len(order_proofs[i])):
                        order_statement = self._state.utils.verifySignature(order_proofs[i][j], self._state.replicaPublicKeys[j]).decode('UTF-8')
                        if (not (order_statement == first_order_statement)):
                            return False
            except:
                return False
        return True

    def check_validity_of_checkpoint_proof(self, checkpoint_proof):
        checkpoint_set = set()
        for i in range(0, len(checkpoint_proof)):
            verification = True
            checkpoint_statement = ''
            try:
                checkpoint_statement = self._state.utils.verifySignature(checkpoint_proof[i], self._state.replicaPublicKeys[i]).decode('UTF-8')
            except Exception:
                verification = False
            if (verification == True):
                checkpoint_set.add(checkpoint_statement)
        if (len(checkpoint_set) > (int((len(self._state.replicaPublicKeys) / 2)) + 1)):
            return False
        return True

    def get_list_of_order_statements(self, order_proof):
        order_statements = []
        for i in range(0, len(order_proof)):
            order_statement = self._state.utils.verifySignature(order_proof[i], self._state.replicaPublicKeys[i]).decode('UTF-8')
            order_statements.append(order_statement)
        return order_statements

    def check_for_prefix(self, order_statements_current, order_statements_successor):
        for i in range(0, len(order_statements_current)):
            if (not (order_statements_current[i] == order_statements_successor[i])):
                return False
        return True

    def check_consistency_of_quorum(self, quorum):
        quorumsize = len(quorum)
        history = self._state.possibleQuorumWedges[quorum[(quorumsize - 1)]].history
        smallestHistorySize = len(history)
        for i in range(0, smallestHistorySize):
            flag = 0
            so_pair = None
            order_statement_list = None
            for j in range((quorumsize - 1), (- 1), (- 1)):
                try:
                    if (flag == 0):
                        history = self._state.possibleQuorumWedges[quorum[j]].history
                        order_statement_list = self.get_list_of_order_statements(history[i])
                        so_pair = self.get_so_pair_from_order_proof(history[i])
                        flag = 1
                    else:
                        history = self._state.possibleQuorumWedges[quorum[j]].history
                        temp_order_statement_list = self.get_list_of_order_statements(history[i])
                        temp_so_pair = self.get_so_pair_from_order_proof(history[i])
                        if (not (temp_so_pair == so_pair)):
                            return False
                        if (self.check_for_prefix(temp_order_statement_list, order_statement_list) == False):
                            return False
                except:
                    return False
        return True

    def get_so_pair_with_request_from_order_statement(self, order_statement):
        so_pair = None
        try:
            order_statement = self._state.utils.verifySignature(order_statement, self._state.replicaPublicKeys[0]).decode('UTF-8')
            strings = order_statement.split(';')
            operation = ((((((strings[0] + ';') + strings[2]) + ';') + strings[3]) + ';') + strings[4])
            slot = int(strings[1])
            so_pair = (slot, operation)
        except:
            pass
        return so_pair

    def get_operations_for_replica(self, quorum):
        quorumsize = len(quorum)
        longesthistory = self._state.possibleQuorumWedges[quorum[0]].history
        longesthistorysize = len(longesthistory)
        so_pairs = []
        operationspending = {}
        for i in range(0, longesthistorysize):
            so_pairs.append(self.get_so_pair_with_request_from_order_statement(longesthistory[i][0]))
        operationspending[quorum[0]] = []
        for i in range(1, quorumsize):
            historysize = len(self._state.possibleQuorumWedges[quorum[i]].history)
            operationspending[quorum[i]] = []
            for j in range(historysize, longesthistorysize):
                operationspending[quorum[i]].append(so_pairs[j])
        return operationspending

    def check_for_same_baseline_of_checkpoint_proof(self, quorum):
        headreplicawedged = self._state.possibleQuorumWedges[quorum[0]]
        headreplicahistory = headreplicawedged.history
        headreplicaslotNo = None
        if (len(headreplicahistory) > 0):
            headreplicaslotNo = self.get_so_pair_from_order_proof(headreplicahistory[0])[0]
        samebaseline = True
        for replica in quorum:
            replicawedged = self._state.possibleQuorumWedges[replica]
            replicalastcheckpointproof = []
            if (len(replicawedged.checkpoint_history) > 0):
                replicalastcheckpointproof = replicawedged.checkpoint_history[(- 1)]
            if (self.check_validity_of_checkpoint_proof(replicalastcheckpointproof) == False):
                return (False, False)
            replicahistory = replicawedged.history
            replicaslotNo = None
            if (len(replicahistory) > 0):
                replicaslotNo = self.get_so_pair_from_order_proof(replicahistory[0])[0]
            if ((not (replicaslotNo == None)) and (headreplicaslotNo == None)):
                return (False, False)
            if ((not (replicaslotNo == None)) and (not (headreplicaslotNo == None)) and (replicaslotNo > headreplicaslotNo)):
                replicasecondlastcheckpointproof = []
                if (len(replicawedged.checkpoint_history) > 1):
                    replicasecondlastcheckpointproof = replicawedged.checkpoint_history[(- 2)]
                if (self.check_validity_of_checkpoint_proof(replicasecondlastcheckpointproof) == False):
                    return (False, False)
                samebaseline = False
            elif ((not (replicaslotNo == None)) and (not (headreplicaslotNo == None)) and (replicaslotNo < headreplicaslotNo)):
                return (False, False)
        return (True, samebaseline)

    def get_so_pair_from_order_proof(self, order_proof):
        so_pair = None
        if (len(order_proof) > 0):
            try:
                order_statement = self._state.utils.verifySignature(order_proof[0], self._state.replicaPublicKeys[0]).decode('UTF-8')
                so_pair = self.get_so_pair_from_order_statement(order_statement)
            except:
                pass
        return so_pair

    def get_operations_for_replica_in_diff(self, quorum):
        quorumsize = len(quorum)
        longesthistory = self._state.possibleQuorumWedges[quorum[0]].history
        longesthistorysize = len(longesthistory)
        so_pairs = []
        slotToIndex = {}
        operationspending = {}
        for i in range(0, longesthistorysize):
            so_pair = self.get_so_pair_with_request_from_order_statement(longesthistory[i][0])
            so_pairs.append(so_pair)
            slotToIndex[so_pair[0]] = i
        operationspending[quorum[0]] = []
        for i in range(1, quorumsize):
            history = self._state.possibleQuorumWedges[quorum[i]].history
            historysize = len(history)
            operationspending[quorum[i]] = []
            try:
                so_pair = self.get_so_pair_with_request_from_order_statement(history[(historysize - 1)][0])
                startingindex = slotToIndex[so_pair[0]]
                for j in range((startingindex + 1), longesthistorysize):
                    operationspending[quorum[i]].append(so_pairs[j])
            except:
                continue
        return operationspending

    def sendResultToClients(self, quorum):
        lastresultstatement = self._state.caughtUpResponses[quorum[0]][1]
        self._state.clients = lastresultstatement.keys()
        clientsToResultMap = {}
        for cid in self._state.clients:
            resultobject = lastresultstatement[cid]
            result = resultobject[0]
            operation_object = resultobject[2]
            resultstatement = ''
            replicaIndex = self._state.replicaToIndexMap[quorum[0]]
            try:
                resultstatement = self._state.utils.verifySignature(resultobject[1], self._state.replicaPublicKeys[replicaIndex])
            except:
                continue
            quorumflag = True
            for i in range(1, len(quorum)):
                try:
                    tempresultobject = self._state.caughtUpResponses[quorum[i]][1][cid]
                    replicaIndex = self._state.replicaToIndexMap[quorum[i]]
                    tempresult = tempresultobject[0]
                    tempresultstatement = ''
                    tempreplicaIndex = self._state.replicaToIndexMap[quorum[i]]
                    tempresultstatement = self._state.utils.verifySignature(tempresultobject[1], self._state.replicaPublicKeys[tempreplicaIndex])
                    if ((not (result == tempresult)) or (not (resultstatement == tempresultstatement))):
                        quorumflag = False
                        break
                except:
                    quorumflag = False
                    break
            if (quorumflag == False):
                continue
            self.output((((('Sending result ' + result) + ' to client ') + str(cid)) + ' from olympus'))
            self.send(('Result from olympus', result, operation_object.requestId), to=self._state.clientIdtoClients[cid])

    def getReplicasFromWedges(self):
        treplicas = self._state.possibleQuorumWedges.keys()
        ind = []
        for replica in treplicas:
            ind.append(self._state.replicaToIndexMap[replica])
        ind.sort()
        freplicas = []
        for i in ind:
            freplicas.append(self._state.indexToReplicaMap[i])
        return freplicas

    def check_for_quorum_and_create_new_replicas(self):
        self._state.createquorumlock = True
        size = (int((len(self._state.replicas) / 2)) + 1)
        tempreplicas = self.getReplicasFromWedges()
        intialsize = len(tempreplicas)
        quorumSets = list(itertools.combinations(tempreplicas, size))
        quorumformed = False
        for quorum in quorumSets:
            if (quorum in self._state.checkedquorums):
                continue
            self._state.checkedquorums.add(quorum)
            validateHistory = True
            for replica in quorum:
                wedged = self._state.possibleQuorumWedges[replica]
                if (self.check_validity_of_history(wedged.history) == False):
                    validateHistory = False
                    break
            if (validateHistory == False):
                continue
            (validity, samebaselineofcheckpointproofs) = self.check_for_same_baseline_of_checkpoint_proof(quorum)
            if (validity == False):
                continue
            operationspending = {}
            if (samebaselineofcheckpointproofs == True):
                consistencyflag = self.check_consistency_of_quorum(quorum)
                if (consistencyflag == False):
                    continue
                operationspending = self.get_operations_for_replica(quorum)
            else:
                operationspending = self.get_operations_for_replica_in_diff(quorum)
            self.output(('Sending catch up messages to quorum: ' + str(quorum)))
            testquorum = quorum
            for replica in quorum:
                self.send(('Catch up', operationspending[replica]), to=replica)
            super()._label('_st_label_2307', block=False)
            replica = None

            def UniversalOpExpr_2308():
                nonlocal replica
                for replica in testquorum:

                    def ExistentialOpExpr_2313(replica):
                        for (_, _, (_ConstantPattern2331_, _, _, _BoundPattern2335_)) in self._OlympusReceivedEvent_3:
                            if (_ConstantPattern2331_ == 'Caught up'):
                                if (_BoundPattern2335_ == replica):
                                    if True:
                                        return True
                        return False
                    if (not ExistentialOpExpr_2313(replica=replica)):
                        return False
                return True
            _st_label_2307 = 0
            self._timer_start()
            while (_st_label_2307 == 0):
                _st_label_2307 += 1
                if UniversalOpExpr_2308():
                    pass
                    _st_label_2307 += 1
                elif self._timer_expired:
                    continue
                    _st_label_2307 += 1
                else:
                    super()._label('_st_label_2307', block=True, timeout=10)
                    _st_label_2307 -= 1
            else:
                if (_st_label_2307 != 2):
                    continue
            if (_st_label_2307 != 2):
                break
            result_set = set()
            for replica in quorum:
                result = self._state.caughtUpResponses[replica][0]
                result_set.add(result)
            if (not (len(result_set) == 1)):
                continue
            else:
                result_hash = result_set.pop()
                self.output(('Quorum successfully formed with replicas: ' + str(quorum)))
                self.sendResultToClients(quorum)
                while True:
                    rep = random.SystemRandom().choice(quorum)
                    self.send('Get running state', to=rep)
                    super()._label('_st_label_2404', block=False)
                    rep = None

                    def ExistentialOpExpr_2405():
                        nonlocal rep
                        for (_, (_, _, rep), (_ConstantPattern2423_, _)) in self._OlympusReceivedEvent_4:
                            if (_ConstantPattern2423_ == 'Running state'):
                                if True:
                                    return True
                        return False
                    _st_label_2404 = 0
                    while (_st_label_2404 == 0):
                        _st_label_2404 += 1
                        if ExistentialOpExpr_2405():
                            _st_label_2404 += 1
                        else:
                            super()._label('_st_label_2404', block=True)
                            _st_label_2404 -= 1
                    else:
                        if (_st_label_2404 != 2):
                            continue
                    if (_st_label_2404 != 2):
                        break
                    temphash = self._state.utils.getHash(str(self._state.replicarunningstate))
                    if (self._state.utils.verifyTwoHash(temphash, result_hash) == True):
                        self.output(('Successful running state recieved at olympus from replica: ' + str(rep)))
                        break
                alloldreplicas = self._state.replicas
                self.createNewConfiguration(self._state.replicarunningstate)
                self.intializeVariables()
                self.send('Kill old replicas', to=alloldreplicas)
                quorumformed = True
                break
        if (quorumformed == True):
            return
        self.output('Quorum not created!! , Trying Again. ')
        actualsize = len(self.getReplicasFromWedges())
        if (actualsize > intialsize):
            self.check_for_quorum_and_create_new_replicas()
        self._state.createquorumlock = False

    def _Olympus_handler_559(self, clientId, p):
        self.send(('Config Response', self._state.replicas, self._state.head, self._state.tail, self._state.isCurrentConfigValid, self._state.replicaPublicKeys), to=p)
    _Olympus_handler_559._labels = None
    _Olympus_handler_559._notlabels = None

    def _Olympus_handler_2504(self, clientid, p):
        self.send(('Config Response', self._state.replicas, self._state.head, self._state.tail, self._state.isCurrentConfigValid, self._state.replicaPublicKeys), to=p)
    _Olympus_handler_2504._labels = None
    _Olympus_handler_2504._notlabels = None

    def _Olympus_handler_2536(self, replica, p):
        self.output(('Reconfiguration request recieved at olympus from replica: ' + str(p)))
        self.output(('Current state ' + str(self._state.currentState)))
        if (not (self._state.currentState == 'Reconfig')):
            self._state.isCurrentConfigValid = False
            self._state.currentState = 'Reconfig'
            self.send('Wedge request', to=self._state.replicas)
    _Olympus_handler_2536._labels = None
    _Olympus_handler_2536._notlabels = None

    def _Olympus_handler_2585(self, client_result, result, result_proof, client, p):
        self.output(('Reconfiguration request recieved at olympus from client: ' + str(p)))
        if (not (self._state.currentState == 'Reconfig')):
            if (self.check_validity_of_result_proof(client_result, result, result_proof) == False):
                self._state.isCurrentConfigValid = False
                self._state.currentState = 'Reconfig'
                self.send('Wedge request', to=self._state.replicas)
    _Olympus_handler_2585._labels = None
    _Olympus_handler_2585._notlabels = None

    def _Olympus_handler_2640(self, wedgedMessage, replica, p):
        self.output(('Wedge response recieved at olympus from replica: ' + str(replica)))
        self._state.wedgeResponseCount += 1
        self._state.possibleQuorumWedges[replica] = wedgedMessage
        if (self._state.wedgeResponseCount >= (int((len(self._state.replicas) / 2)) + 1)):
            if ((self._state.isCurrentConfigValid == False) and (self._state.createquorumlock == False)):
                self.check_for_quorum_and_create_new_replicas()
    _Olympus_handler_2640._labels = None
    _Olympus_handler_2640._notlabels = None

    def _Olympus_handler_2702(self, state_hash, lastresultstatements, replica, p):
        self.output(('Caught up message response recieved at olympus from replica: ' + str(replica)))
        self._state.caughtUpResponses[replica] = (state_hash, lastresultstatements)
    _Olympus_handler_2702._labels = None
    _Olympus_handler_2702._notlabels = None

    def _Olympus_handler_2733(self, running_state, p):
        self.output(('Running state recieved at olympus from replica: ' + str(p)))
        self._state.replicarunningstate = running_state
    _Olympus_handler_2733._labels = None
    _Olympus_handler_2733._notlabels = None
